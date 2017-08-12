# coding=utf-8
import json
token="{\"access_token\":\"Iwm0etmmOqtXcPvGZp-_A8V28RmvLqxy4mOUs5AYppuNgCB04G0m_TNxv4xvphsWfPg7TP-9Ekyi8YNicArC6WX1Npu0dn4B9h4Qa8vSSz5rzmktS0SxN_hmixYVmFSfQYSdAFAMUO\",\"expires_in\":7200}"
expires_in = json.loads(token)['expires_in']
print(expires_in)