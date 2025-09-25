const Youtube = function(apiKey, $box) {
    const MAX_LOADS   = 30; // 조회할 결과 수
    const MAX_RESULTS = 10;  // 원하는 결과 수

    async function getUploadPlaylistId(channelId) {
        const url = `https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=${channelId}&key=${apiKey}`;
        const res = await fetch(url);
        const data = await res.json();
        return data.items[0].contentDetails.relatedPlaylists.uploads;
    }

    async function getVideosFromPlaylist(playlistId) {
        const url = `https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=${MAX_LOADS}&playlistId=${playlistId}&key=${apiKey}`;
        const res = await fetch(url);
        const data = await res.json();
        const searched = data.items.map(item => item.contentDetails.videoId);
        const set = new Set();
        while(set.size < MAX_RESULTS) {
            let idx = parseInt(Math.random() * searched.length);
            set.add(idx);
        }
        const result = [];
        set.forEach(v => result.push(searched[v]))
        // for(let v in set) {
        //     result.push(searched[v])
        // }
        return result;
    }

    async function getVideoDetails(videoIds) {
        const ids = videoIds.join(',');
        const url = `https://www.googleapis.com/youtube/v3/videos?part=contentDetails,snippet&id=${ids}&key=${apiKey}`;
        const res = await fetch(url);
        const data = await res.json();
        return data.items.map(item => {
            const duration = item.contentDetails.duration;
            const seconds = parseISODuration(duration);
            return {
            title: item.snippet.title,
            thumb: item.snippet.thumbnails.standard.url,
            videoId: item.id,
            duration: seconds,
            url: `https://www.youtube.com/shorts/${item.id}`,
            embed: `https://www.youtube.com/embed/${item.id}`,
            isShort: seconds <= 60
            };
        }).filter(video => video.isShort).slice(0, 5);
    }

    // ISO 8601 Duration (e.g., PT45S, PT1M2S, etc.) → seconds
    function parseISODuration(iso) {
        const regex = /PT(?:(\d+)M)?(?:(\d+)S)?/;
        const matches = iso.match(regex);
        const minutes = parseInt(matches[1] || '0', 10);
        const seconds = parseInt(matches[2] || '0', 10);
        return minutes * 60 + seconds;
    }

    async function fetchShortsFromChannel(channelId) {
        try {
            const playlistId = await getUploadPlaylistId(channelId);
            const videoIds = await getVideosFromPlaylist(playlistId);
            const shorts = await getVideoDetails(videoIds);
            // console.log('Found Shorts:', shorts);

            $box.innerHTML = "";
            shorts.forEach(short => {
                const div = document.createElement('div');
                div.innerHTML = `
                    <iframe width="170" height="315" 
                        src="${short.embed}" 
                        title="${short.title}" 
                        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                        allowfullscreen>
                    </iframe>
                `;
                $box.appendChild(div);
            });
        } catch (err) {
            console.error('Error fetching Shorts:', err);
        }
    }

    return fetchShortsFromChannel;
}