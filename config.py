from authomatic.providers import oauth2

# 希望設計流程來保全 consumer_key 與 consumer_secret 字串
CONFIG = {
        'google': {
            'class_': oauth2.Google,
            'consumer_key': '519961530979-4k3spnt0eiqn5tgovdv2cue0tqobtaai.apps.googleusercontent.com',
            'consumer_secret': 'qO_31mCfr6_b7bnYtZdD6xox',
            #'scope': oauth2.Google.user_info_scope
            # 以下將只檢視(瞭解您在 Google 上的身分)與(檢視電子郵件地址)
            'scope': ['email']
        }
    }