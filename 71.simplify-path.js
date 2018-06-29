/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    let paths = [];
    path.split("/").forEach(token => {
        if (token == "..") {
            paths.pop();
        } else if (token != "." && token != "") {
            paths.push(token);
        }
    });
    return "/" + paths.join("/");
};