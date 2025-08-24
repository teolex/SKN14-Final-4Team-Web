// providers.js
const OAUTH_PROVIDERS = {
    google: {
        authUrl      : "https://accounts.google.com/o/oauth2/v2/auth",

        client_id    : GOOGLE_CLIENT_ID,
        scope        : "openid profile email",
        redirect_uri : "http://" + DOMAIN + "/user/sns_login/google",
        response_type: "code"
    },
};

function loginWith(provider) {
    const cfg = OAUTH_PROVIDERS[provider];
    if (!cfg) throw new Error("Unknown provider: " + provider);

    const params = new URLSearchParams(cfg);

    window.location.href = `${cfg.authUrl}?${params.toString()}`;
}

[...document.getElementsByClassName("sns-login-btn")]
            .forEach((e,i) => {
                const provider = e.firstChild.classList.value.replace(/^.*fa-([^ ]+.*)/g, "$1");
                e.addEventListener("click", () => loginWith(provider));
            });