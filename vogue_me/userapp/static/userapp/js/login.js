// providers.js
const OAUTH_PROVIDERS = {
    google: {
        authUrl : "https://accounts.google.com/o/oauth2/v2/auth",
        params  : {
            client_id     : GOOGLE_CLIENT_ID,
            redirect_uri  : "http://" + DOMAIN + "/user/sns_login/google",
            response_type : "code",
            scope         : "openid profile email",
        }
    },
    naver: {
        authUrl : "https://nid.naver.com/oauth2.0/authorize",
        params  : {
            client_id     : NAVER_CLIENT_ID,
            redirect_uri  : "http://" + DOMAIN + "/user/sns_login/naver",
            response_type : "code",
        }
    },
    // kakao: {     // 카카오 로그인 API 는 이메일/이름을 받으려면 비즈니스 앱 신청이 필수.
    //     authUrl : "https://kauth.kakao.com/oauth/authorize",
    //     params  : {
    //         client_id     : KAKAO_CLIENT_ID,
    //         redirect_uri  : "http://" + DOMAIN + "/user/sns_login/kakao",
    //         response_type : "code",
    //         scope         : "openid,profile_image",
    //         prompt        : "login"
    //     }
    // },
};

function loginWith(provider) {
    const cfg = OAUTH_PROVIDERS[provider];
    if (!cfg) throw new Error("Unknown provider: " + provider);

    const params = new URLSearchParams(cfg.params);

    window.location.href = `${cfg.authUrl}?${params.toString()}`;
}

[...document.getElementsByClassName("sns-login-btn")]
            .forEach((e,i) => {
                const provider = e.dataset.sns;
                e.addEventListener("click", () => loginWith(provider));
            });