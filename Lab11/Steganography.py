#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-04-17 20:23:49 -0400 (Sun, 17 Apr 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab11/Steganography.py $
# $Revision: 90660 $

import numpy as np
import base64
import zlib
import re


class Payload:

    def __init__(self, img=None, compressionLevel=-1, xml=None):
        self.img = img
        self.compressionLevel = compressionLevel
        self.xml = xml

        if self.img is None and self.xml is None:
            raise ValueError
        if self.compressionLevel < -1 or self.compressionLevel > 9:
            raise ValueError
        if type(self.xml) is not str and self.xml is not None:
            raise TypeError
        if not isinstance(self.img, np.ndarray) and self.xml is None:
            raise TypeError

        if self.compressionLevel == -1:
            comp = "False"
        else:
            comp = "True"

        i_type, col, row, comp2 = self.getInfo(img, xml)

        if self.xml is None:
            payload = self.getPayload(img, i_type, self.compressionLevel)
            self.xml = '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="{}" size="{},{}" compressed="{}">\n{}' \
                       '\n</payload>'.format(i_type, col, row, comp, payload)
        if self.img is None:
            self.img = self.getImg(self.xml, i_type, col, row, comp2)

    def getInfo(self, img, xml):
        if xml is None:
            if len(img.shape) == 3:
                return "Color", img.shape[0], img.shape[1], None
            if len(img.shape) == 2:
                return "Gray", img.shape[0], img.shape[1], None
        else:
            i_type = re.search(r"type=\"(.*?)\"", xml)
            size = re.search(r"size=\"([\d]+),([\d]+)\"", xml)
            comp = re.search(r"compressed=\"(.*?)\"", xml)
            return i_type.group(1), size.group(1), size.group(2), comp.group(1)

    def getPayload(self, img, i_type, comp):
        if i_type == "Color":
            flat_a = list(img.flat)
            payload = flat_a[::3] + flat_a[1::3] + flat_a[2::3]
            if comp > -1:
                payload = zlib.compress(bytes(payload), comp)
            payload = base64.b64encode(bytes(payload)).decode("UTF-8")
            return payload
        elif i_type == "Gray":
            if comp > -1:
                payload = zlib.compress(bytes(img.flat), comp)
                payload = base64.b64encode(bytes(payload)).decode("UTF-8")
            else:
                payload = base64.b64encode(bytes(img.flat)).decode("UTF-8")
            return payload

    def getImg(self, xml, i_type, col, row, comp):
        payload = re.search(r">\s(.*?)\s<", xml)
        payload = payload.group(1)
        decoded = base64.decodebytes(bytearray(payload, 'utf-8'))
        if comp == "True":
            decoded = zlib.decompress(decoded)
        if i_type == "Gray":
            data = np.array(list(decoded))
            data = np.reshape(data, (int(col), int(row)))
            return data
        elif i_type == "Color":
            rgb_len = int(len(decoded) / 3)
            r = list(decoded[0:rgb_len])
            g = list(decoded[rgb_len: rgb_len*2])
            b = list(decoded[rgb_len*2:])
            data = [list(a) for a in zip(r, g, b)]
            data = np.reshape(np.array(data), (int(col), int(row), 3))
            return data


class Carrier:

    def __init__(self, img):
        if isinstance(img, np.ndarray):
            self.img = img
        else:
            raise TypeError

    def payloadExists(self):
        pay = []
        if len(self.img.shape) == 2:
            for i in range(40):
                pay.append(self.img.flat[i] & 1)
            text = "".join(chr(int("".join(map(str, pay[i:i+8])), 2)) for i in range(0, len(pay), 8))
            if "<?xml" == text:
                return True
            else:
                return False
        else:
            for i in range(0, 120, 3):
                pay.append(self.img.flat[i] & 1)
            text = "".join(chr(int("".join(map(str, pay[i:i+8])), 2)) for i in range(0, len(pay), 8))
            if "<?xml" == text:
                return True
            else:
                return False

    def clean(self):
        new = np.copy(self.img)
        new = new & ~1
        return new

    def embedPayload(self, payload, override=False):
        if override is False:
            if self.payloadExists():
                raise Exception
        if not isinstance(payload, Payload):
            raise TypeError
        if payload.img.size * 8 > self.img.size:
            raise ValueError
        new = np.copy(self.img)

        if len(self.img.shape) == 2:
            bin_p = bin(int.from_bytes(payload.xml.encode(), 'big'))
            for i in range(0, len(bin_p)):
                if bin_p[i] == "0":
                    new.flat[i] &= ~1
                elif bin_p[i] == "1":
                    new.flat[i] |= 1
            return new
        elif len(self.img.shape) == 3:
            n_pass = 0
            count = 0
            rgb_len = int(self.img.size / 3)
            bin_p = bin(int.from_bytes(payload.xml.encode(), 'big'))
            for i in range(len(bin_p)):
                if bin_p[i] == "0":
                    new.flat[count*3+n_pass] &= ~1
                elif bin_p[i] == "1":
                    new.flat[count*3+n_pass] |= 1
                if count >= rgb_len - 1:
                    count = -1
                    n_pass += 1
                count += 1

            return new

    def extractPayload(self):
        if not self.payloadExists():
            raise Exception
        pay = np.copy(self.img)
        pay &= 1
        if len(self.img.shape) == 3:
            pay = list(pay.flat)
            pay_c = pay[::3] + pay[1::3] + pay[2::3]
            pay_b = np.packbits(np.array(pay_c).astype(int))
            pay_f = pay_b[pay_b < 128]
            text = np.array(pay_f, dtype=np.int8).tostring().decode("ascii")
            r = Payload(None, -1, text)
            return r
        else:
            pay_b = np.packbits(pay.astype(int))
            pay_f = pay_b[pay_b < 128]
            text = np.array(pay_f, dtype=np.int8).tostring().decode("ascii")
            r = Payload(None, -1, text)
            return r




