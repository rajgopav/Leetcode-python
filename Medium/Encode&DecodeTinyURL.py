class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        url = longUrl[9:]
        last = url.split('/')[-1]
        encode = last.encode('UTF-8', 'strict')

        return longUrl.replace(last, encode)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        url = shortUrl[9:]
        last = url.split('/')[-1]
        decode = last.decode('UTF-8', 'strict')
        return shortUrl.replace(last, decode)

if __name__ == '__main__':
    codec = Codec()
    codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))