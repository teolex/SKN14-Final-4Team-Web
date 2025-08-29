const _valid = ($ele, isValid) => {
    let remover = isValid ? "is-invalid" : "is-valid";
    let adder   = isValid ? "is-valid" : "is-invalid";
    $ele.classList.remove(remover);
    $ele.classList.add(adder);
    return isValid;
};


const init_email_dup = function(apiUrl) {
    const $csrf  = document.getElementsByName("csrfmiddlewaretoken")[0];
    const $email = document.getElementsByName("email")[0];
    const $msg   = document.querySelector("input[name=email] + .invalid-feedback");
    let timeout;
    $email.addEventListener("input", (e) => {
        clearTimeout(timeout);
        e.target.classList.remove("is-valid", "is-invalid");

        timeout = setTimeout(() => {
            if(! /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i.test(e.target.value)) {
                _valid(e.target, false);
                $msg.innerText = "이메일 주소를 확인해주세요.";
                return;
            }

            fetch(apiUrl, {
                method : "POST",
                cache  : "no-cache",
                headers: { "Content-Type": "application/json", "X-CSRFToken": $csrf.value },
                body: JSON.stringify({ email : e.target.value })
            }).then(resp => { return resp.json();
            }).then(data => {
                const isDup = data["already_exist"];
                if( isDup ) $msg.innerText = "이미 가입된 계정입니다.";
                _valid(e.target, !isDup);
            })
        }, 1000);
    });
};


const init_passwd_rule_checker = function(){
    const $rules = document.getElementById("passwordRules");
    const $pw1   = document.getElementsByName("password1")[0];
    const $pw2   = document.getElementsByName("password2")[0];
    let timeout1, timeout2;
    $pw1.addEventListener("input", e => {
        clearTimeout(timeout1);
        timeout1 = setTimeout(() => {
            let all_passed = true;
            const value = e.target.value;
            const rules = {
                lower   : /[a-z]/,
                upper   : /[A-Z]/,
                number  : /[0-9]/,
                special : /[!@#$%^&*()]/,
                length  : /[a-zA-Z0-9!@#$%^&*()]{8,}/
            };

            for (const [key, regex] of Object.entries(rules)) {
                const element = document.getElementById(`rule-${key}`);
                if (regex.test(value)) {
                    element.classList.remove("text-danger");
                    element.classList.add("text-success");
                    element.textContent = `✅ ${element.textContent.slice(2)}`;
                } else {
                    element.classList.remove("text-success");
                    element.classList.add("text-danger");
                    element.textContent = `❌ ${element.textContent.slice(2)}`;
                    all_passed = false;
                }
            }
            $rules.classList.toggle("d-none", all_passed);
            _valid($pw1, all_passed);
            _valid($pw2, $pw1.value === $pw2.value);
        }, 500);
    });
    $pw2.addEventListener("input", e => {
        clearTimeout(timeout2);
        timeout2 = setTimeout(() => _valid(e.target, $pw1.value === e.target.value), 200);
    });
};


const init_name_checker = function($e){
    let timeout;
    $e.addEventListener("input", e => {
        clearTimeout(timeout);
        timeout = setTimeout(() => _valid(e.target, e.target.value.length > 0), 500);
    });
};