class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = []
        for token in path.split("/"):
            if paths and token == "..":
                paths.pop()
            elif token != ".." and token != "." and token != "":
                paths.append(token)
        return "/" + "/".join(paths)