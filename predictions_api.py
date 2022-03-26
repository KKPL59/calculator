from kivy.network.urlrequest import UrlRequest
import base64
import json


class ImgHere:
    api = 'https://imgpred.herokuapp.com/test'

    def __init__(self, img_1x784):
        """Doknuje predykcji na podtawie otrzymanego zdjęcia."""

        self.predictions = img_1x784

        with open("digit.png", "rb") as f:
            self.im_bytes = f.read()
        self.im_b64 = base64.b64encode(self.im_bytes).decode("utf8")

    def get_prediction(self):
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        self.payload = json.dumps({"image": self.im_b64, "other_key": "value"})
        self.req = UrlRequest(url=self.api, req_body=self.payload, req_headers=self.headers)

        self.req.wait()

        return self.req.result

# img = cv2.imread("1_YpijSnfbzpF2118eYUeNCg.png")
#
# imghere = ImgHere(img)
# print(imghere.get_prediction()[1])
