#by bafomet
import base64, codecs
magic = 'IyEvdXNyL2Jpbi9weXRob24KIy0qLSBjb2Rpbmc6IHV0Zi04IC0qLQojRGV2ZWxvcGVyIGJ5IEJhZm9tZXQKaW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IG9zCmltcG9ydCBzeXMKaW1wb3J0IHJlYWRsaW5lCiNzZXQgY29sb3IKV0hTTCA9ICdcMDMzWzE7MzJtJwpFTkRMID0gJ1wwMzNbMG0nClJFREwgPSAnXDAzM1swOzMxbScKR05TTCA9ICdcMDMzWzE7MzRtJwoKb3Muc3lzdGVtKCJwcmludGYgJ1wwMzNdMjtPU0lOVCBBdHRhY2sgbW9kXGEnIikKb3Muc3lzdGVtKCdjbGVhcicpCnN1YnByb2Nlc3MuY2FsbCgicHl0aG9uMyBiYW5uZXIucHkiLCBzaGVsbD1UcnVlKQpwYWdlXzEgPSAnJycgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgezB9WyB7MX0wMXswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgICAgICAgezB9WyB7MX0xNnswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgICAgICAgezB9WyB7MX0zMXswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgIHsxfdCe0LbQuNC00LDQudGC0LUg0LIg0LLQtdGA0YHQuNGP0YUgNC4wINC4INCy0YvRiNC1Li4uCiAgezB9WyB7MX0wMnswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgICAgICAgezB9WyB7MX0xN3swfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgICAgICAgezB9WyB7MX0zMnswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgIHsxfdCR0YPQtNGDINC/0L7Qv9C+0LvQvdGP0YLRjCDQv9C+INC80LXRgNC1INGB0LLQvtCx0L7QtNC90L7Qs9C+INCy0YDQtdC80LXQvdC4LgogIHswfVsgezF9MDN7MH0gXSB7Mn3QodCy0L7QsdC+0LTQvdGL0Lkg0YHQu9C+0YIuLi4gICAgICAgICAgICAgIHswfVsgezF9MTh7MH0gXSB7Mn3QodCy0L7QsdC+0LTQvdGL0Lkg0YHQu9C+0YIuLi4gICAgICAgICAgICAgIHswfVsgezF9MzN7MH0gXSB7Mn3QodCy0L7QsdC+0LTQvdGL0Lkg0YHQu9C+0YIuLi4KICB7MH1bIHsxfTA0ezB9IF0gezJ90KHQstC+0LHQvtC00L3Ri9C5INGB0LvQvtGCLi4uICAgICAgICAgICAgICB7MH1bIHsxfTE5ezB9IF0gezJ90KHQstC+0LHQvtC00L3Ri9C5INGB0LvQvtGCLi4uICAgICAgICAgICAgICB7MH1bIHsxfTM0ezB9IF0gezJ90KHQstC+0LHQvtC00L3Ri9C5INGB0LvQvtGCLi4uCiAgezB9WyB7MX0wNXswfSBdIHsyfdCh0LL'
love = 'DigPk0Y7DgAP90LiDhFQEtqP70Y7Etv4hYvNtVPNtVPNtVPNtVPNtrmO9JlO7ZK0lZUfjsFOqVUflsqPu0YYDigPk0Y7DgAP90LiDhFQEtqP70Y7Etv4hYvNtVPNtVPNtVPNtVPNtrmO9JlO7ZK0mAKfjsFOqVUflsqPu0YYDigPk0Y7DgAP90LiDhFQEtqP70Y7Etv4hYtbtVUfjsIftrmS9ZQM7ZU0tKFO7Za3DbqPl0Y7DfqP+0YGDiqTY0Yxt0LUDh9P+0LVhYv4tVPNtVPNtVPNtVPNtVUfjsIftrmS9ZwS7ZU0tKFO7Za3DbqPl0Y7DfqP+0YGDiqTY0Yxt0LUDh9P+0LVhYv4tVPNtVPNtVPNtVPNtVUfjsIftrmS9ZmM7ZU0tKFO7Za3DbqPl0Y7DfqP+0YGDiqTY0Yxt0LUDh9P+0LVhYv4XVPO7ZU1oVUfksGN3rmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hVPNtVPNtVPNtVPNtVPO7ZU1oVUfksGVlrmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hVPNtVPNtVPNtVPNtVPO7ZU1oVUfksGZ3rmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hPvNtrmO9JlO7ZK0jBUfjsFOqVUflsqPu0YYDigPk0Y7DgAP90LiDhFQEtqP70Y7Etv4hYvNtVPNtVPNtVPNtVPNtrmO9JlO7ZK0lZ3fjsFOqVUflsqPu0YYDigPk0Y7DgAP90LiDhFQEtqP70Y7Etv4hYvNtVPNtVPNtVPNtVPNtrmO9JlO7ZK0mBUfjsFOqVUflsqPu0YYDigPk0Y7DgAP90LiDhFQEtqP70Y7Etv4hYvNXVPO7ZU1oVUfksGN5rmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hVPNtVPNtVPNtVPNtVPO7ZU1oVUfksGV0rmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hVPNtVPNtVPNtVPNtVPO7ZU1oVUfksGZ5rmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hVNbtVUfjsIftrmS9ZGO7ZU0tKFO7Za3DbqPl0Y7DfqP+0YGDiqTY0Yxt0LUDh9P+0LVhYv4tVPNtVPNtVPNtVPNtVUfjsIftrmS9ZwI7ZU0tKFO7Za3DbqPl0Y7DfqP+0YGDiqTY0Yxt0LUDh9P+0LVhYv4tVPNtVPNtVPNtVPNtVUfjsIftrmS9AQO7ZU0tKFO7Za3DbqPl0Y7DfqP+0YGDiqTY0Yxt0LUDh9P+0LVhYv4XVPO7ZU1oVUfksGRkrmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hVPNtVPNtVPNtVPNtVPO7ZU1oVUfksGV2rmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hVPNtVPNtVPNtVPNtVPO7ZU1oVUfksGDkrmO9VS0trmW90XUDfgP+0YUDigP00Y3Ev9P5VATO0YiDigTPYv4hPvNtrmO9JlO7ZK0kZafjsFOqVUflsqPu0YYDigPk0Y7DgAP90LiDhFQEtqP70Y7Etv4hYvNtVPNtVPNtVPNtVPNtrmO9JlO7ZK0lA3fjsFOqVUflsqPu0YYDig'
god = 'Cx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgICAgICAgezB9WyB7MX00MnswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLgogIHswfVsgezF9MTN7MH0gXSB7Mn3QodCy0L7QsdC+0LTQvdGL0Lkg0YHQu9C+0YIuLi4gICAgICAgICAgICAgIHswfVsgezF9Mjh7MH0gXSB7Mn3QodCy0L7QsdC+0LTQvdGL0Lkg0YHQu9C+0YIuLi4gICAgICAgICAgICAgIHswfVsgezF9NDN7MH0gXSB7Mn3QodCy0L7QsdC+0LTQvdGL0Lkg0YHQu9C+0YIuLi4KICB7MH1bIHsxfTE0ezB9IF0gezJ90KHQstC+0LHQvtC00L3Ri9C5INGB0LvQvtGCLi4uICAgICAgICAgICAgICB7MH1bIHsxfTI5ezB9IF0gezJ90KHQstC+0LHQvtC00L3Ri9C5INGB0LvQvtGCLi4uICAgICAgICAgICAgICB7MH1bIHsxfTQ0ezB9IF0gezJ90KHQstC+0LHQvtC00L3Ri9C5INGB0LvQvtGCLi4uCiAgezB9WyB7MX0xNXswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgICAgICAgezB9WyB7MX0zMHswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLiAgICAgICAgICAgICAgezB9WyB7MX00NXswfSBdIHsyfdCh0LLQvtCx0L7QtNC90YvQuSDRgdC70L7Rgi4uLgogIAogIHsxfeKUlOKUgOKUgD4gezB9IHsyfdCe0LHRgNCw0YLQvdC+INCyIE9TSU5UIE1lbnUuLi4uIHswfVt7MX0gODggezB9XXswfSAgICAgICAgezF94pSU4pSA4pSAPiB7MH0gezJ90J7Rh9C40YHRgtC40YLRjC4uLiAgezB9W3sxfSA2NiB7MH1dezB9CiAgCicnJy5mb3JtYXQoR05TTCwgUkVETCwgV0hTTCkKZGVmIG1haW4oKToKICAgIHByaW50KHBhZ2VfMSkKICAgIG9wdGlvbiA9IGlucHV0KFJFREwgKyAiICDilJTilIDilIA+IiArIEVOREwgKyIg0JLRi9Cx0LXRgNC40YLQtSDQvtC/0YbQuNGOIDogIiArRU5ETCArICIgIikKICAgIAogICAgd2hpbGUoMSk6CiAgICAgICAgaWYgb3B0aW9uID09ICc4OCc6CiAgICAgICAgICAgIHByaW50KCIiKQogICAgICAgICAgICBwcmludCgoInsxfVsgezB9K3sxfSBdezJ9INCS0YvQv9C+0LvQvdGP0LXQvCDQvtCx0YDQsNGC0L3Ri9C5INC/0LXRgNC10YXQvtC0LiIpLmZvcm1hdChSRURMLCBHTlNMLCBXSFNMKSkKICAgICAgICAgICAgb3Muc3lzdGVtKCJleGl0IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiY2QgY29yZTtweXRob24zIGJhbm5lci5weSIpCiAgICAgICAgICAgIGV4aXQoKQogICAgICAgICAgICBvcHRpb24gPSBpbnB1dChFTkRMICsgIiIrR05TTCsiWyIrUkVETCArICIgbWVudSAiICsgR05TTCArI'
destiny = 'PWqVvgSGxEZVPftVvN6VvxXVPNtVPNtVPNtVPNtPvNtVPNtVPNtMJkcMvOipUEco24tCG0tWmNkWmbXVPNtVPNtVPNtVPNtpUWcoaDbXPW7ZK1oVUfjsFg7ZK0tKKflsFQDa9P10LQDgqTS0Y7DgP4hYafmsFVcYzMipz1uqPuFEHEZYPOUGyAZYPOKFSAZYPOSGxEZXFxXVPNtVPNtVPNtVPNtMKucqPtcPvNtVPNtVPNtVPNtVTWlMJSePvNtVPNtVPNtVPNtVNbtVPNtVPNtVTIfnJLto3O0nJ9hVQ09VPpjZvp6PvNtVPNtVPNtVPNtVUOlnJ50XPtvrmS9JlO7ZU0ermS9VS17Za0t0W/DgqTN0YKEuqP+0YDhYv57Z30vXF5zo3WgLKDbHxIRGPjtE05GGPjtI0uGGPjtEH5RGPxcPvNtVPNtVPNtVPNtVTI4nKDbXDbtVPNtVPNtVPNtVPOvpzIunjbtVPNtVPNtVPNtVPNXVPNtVPNtVPOyoTyzVT9jqTyiovN9CFNaZQZaBtbtVPNtVPNtVPNtVPOjpzyhqPtbVafksIftrmO9X3fksFOqrmW9VAPs0YKEtAP10LKDigP0Yv4hrmA9VvxhMz9loJS0XSWSERjfVRqBH0jfVSqVH0jfVRIBERjcXDbtVPNtVPNtVPNtVPOyrTy0XPxXVPNtVPNtVPNtVPNtLaWyLJfXVPNtVPNtVPNtVPNtPvNtVPNtVPNtMJkcMvOipUEco24tCG0tWmN0WmbXVPNtVPNtVPNtVPNtpUWcoaDbXPW7ZK1oVUfjsFg7ZK0tKKflsFQDa9P10LQDgqTS0Y7DgP4hYafmsFVcYzMipz1uqPuFEHEZYPOUGyAZYPOKFSAZYPOSGxEZXFxXVPNtVPNtVPNtVPNtMKucqPtcPvNtVPNtVPNtVPNtVTWlMJSePvNtVPNtVPNtVPNtVNbtVPNtVPNtVTIfnJLto3O0nJ9hVQ09VPpjAFp6PvNtVPNtVPNtVPNtVUOlnJ50XPtvrmS9JlO7ZU0ermS9VS17Za0t0W/DgqTN0YKEuqP+0YDhYv57Z30vXF5zo3WgLKDbHxIRGPjtE05GGPjtI0uGGPjtEH5RGPxcPvNtVPNtVPNtVPNtVTI4nKDbXDbtVPNtVPNtVPNtVPOvpzIunjbtVPNtVPNtVPNtVPNXVPNtVPNtVPOyoTyzVT9jqTyiovN9CFNaAwLaBtbtVPNtVPNtVPNtVPOjpzyhqPtbVafksIftrmO9X3fksFOqrmW9VAPs0YKEtAP10LKDigP0Yv4hrmA9VvxhMz9loJS0XSWSERjfVRqBH0jfVSqVH0jfVRIBERjcXDbtVPNtVPNtVPNtVPOipl5mrKA0MJ0bVzAfMJSlVvxXVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWjrKEbo24mVTAipzHhpUxvXDbtVPNtVPNtVPNtVPOyrTy0XPxXVPNtVPNtVPNtVPNtLaWyLJfXVPNtVPNtVPNtVPNtVPNXVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPOipl5mrKA0MJ0bVaO5qTuiowZtL29lMF5jrFVcPaElrGbXVPNtVT1unJ4bXDbXMKuwMKO0VRgyrJWiLKWxFJ50MKWlqKO0BtbtVPNtp3ymYzI4nKDbZFxXMKuwMKO0VRgyrJWiLKWxFJ50MKWlqKO0BtbtVPNtVPNtVUOlnJ50VPtvD3EloPgQVUOlMKAmMJDhYv4vXDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))