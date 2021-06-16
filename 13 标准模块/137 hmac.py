from datetime import datetime
import hashlib
import hmac

key = 'you-never-know'
msg = datetime.utcnow().strftime('%Y-%m-%d')

# 都需要编码，不然报错
m = hmac.new(key.encode(), msg.encode(), hashlib.sha1)
signature = m.hexdigest()
print(signature)
