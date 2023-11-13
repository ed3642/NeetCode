import json

class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return json.dumps(strs)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        return json.loads(s)
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))