import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from apiapp.models import ChatHistory


# Create your views here.

@login_required
def ask_api(request):
    raw_data  = request.body.decode('utf-8')
    json_data = json.loads(raw_data)

    msg     = json_data['msg']
    user_id = request.user.id
    ai_id   = request.session.get('ai_id', 1)
    chat    = _save_chat(user_id, msg, ai_id)

    api_dict = _get_result(msg)
    result = {
        "type"  : "ai",
        "msg1"  : api_dict['style_text'],
        "msg2"  : api_dict['optional_text'],
        "voice" : api_dict['voice'],
        "time"  : chat.time,
        "list"  : [
            {
                "id"        : item["look_id"],
                "look_name" : item["look_style"],
                "image"     : item["model_img_url"],
                "look_desc" : item["reason_selected"],
            }
            for item in api_dict['results']
        ]
    }
    return JsonResponse(result)

def _save_chat(user_id, style_text, ai_id=1, talker_type="user", optional_text=None, voice_url=None):
    return ChatHistory.objects.create(
        user_id         = user_id,
        influencer_id   = ai_id,
        style_text      = style_text,
        talker_type     = talker_type,
        optional_text   = optional_text,
        voice_url       = voice_url
    )

def _get_result(msg:str) -> dict:
    # 가라 데이터 반환
    import os
    from django.conf import settings
    dummy_json = os.path.join(settings.BASE_DIR, "static/dummy", 'dummy_result.json')
    with open(dummy_json, "r", encoding="utf-8") as f:
        return json.load(f)