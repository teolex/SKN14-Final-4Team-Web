const $room = document.getElementById("chat-area");
const $tmplChat = document.getElementById("tmpl-chat").content;
const TYPE = {USER: "user", AI: "ai"};
Object.freeze(TYPE);

const curTime = () => {
    let now = new Date();
    let hour = now.getHours();
    let min = now.getMinutes();
    let ampm = hour >= 12 ? "PM" : "AM";
    hour = hour % 12 || 12;
    hour = (hour < 10 ? "0" : "") + hour;
    min = (min < 10 ? "0" : "") + min;
    return `${hour}:${min} ${ampm}`;
};

const addChat = (data) => {
    let type = data["type"];
    let msg1 = data["msg1"] || data["msg"];
    let msg2 = data["msg2"];
    let time = data["time"] || curTime();
    let profileImage = AI_INFO.image;
    let talkerName = AI_INFO.name;

    type = Object.values(TYPE).includes(type) ? type : TYPE.AI;
    if (type === TYPE.USER) {
        profileImage = USER_INFO.image;
        talkerName = USER_INFO.name;
    }

    let $chat = $tmplChat.cloneNode(true).querySelector(".chat");
    $chat.classList.add(type);
    $chat.querySelector(".profile-image").src = profileImage;
    $chat.querySelector(".profile-image").alt = talkerName;
    $chat.querySelector(".talker-name").innerText = talkerName;
    $chat.querySelector(".text").innerHTML = msg1.replace(/\r/g, "").replace(/\n/g, "<br/>");
    $chat.querySelector(".chat-time").innerText = time;

    // 스타일 결과와 옵션 텍스트, 음성 제거 (기본 채팅만 사용)
    $chat.querySelector(".style_result").remove();
    $chat.querySelector(".text.optional").remove();
    $chat.querySelector(".voice").remove();

    $room.appendChild($chat);
    $chat.scrollIntoView({behavior: "smooth", block: "end"});
};

// 채팅 전송 기능
const $userInput = document.querySelector(".user_input");
const $sendBtn = document.querySelector(".send-btn");

$sendBtn.addEventListener("click", e => {
    const msg = $userInput.value.trim();
    if (!msg) return;

    const userParam = {
        "type": TYPE.USER,
        "msg1": msg,
    };

    addChat(userParam);
    $userInput.value = "";

    // AI 응답 시뮬레이션
    setTimeout(() => {
        const aiResponses = [
            "좋은 질문이네요! 친환경 패션에 대해 알려드릴게요 🌱",
            "지속가능한 소재로 만든 옷을 추천해드릴게요!",
            "환경을 생각하는 스타일링을 도와드리겠습니다 ✨",
            "재활용 소재를 활용한 멋진 코디는 어떠세요?",
        ];
        const randomResponse = aiResponses[Math.floor(Math.random() * aiResponses.length)];

        addChat({
            type: TYPE.AI,
            msg1: randomResponse
        });
    }, 1000);
});

$userInput.addEventListener("keydown", e => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        $sendBtn.click();
    }
});

$userInput.addEventListener("focus", e => e.target.placeholder = "");
$userInput.addEventListener("blur", e => e.target.placeholder = "메시지를 입력하세요...");

// 텍스트 영역 자동 높이 조절
$userInput.addEventListener("input", function() {
    this.style.height = "auto";
    this.style.height = Math.min(this.scrollHeight, 100) + "px";
});