/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let trap = 0;
    let max_height = 0, max_height_pos = 0;
    for (let i = 0; i < height.length; i++) {
        if (height[i] > max_height) {
            max_height = height[i];
            max_height_pos = i;
        }
    }
    for (let max_h = 0, i = 0; i < max_height_pos; i++) {
        let h = height[i];
        if (h > max_h) {
            max_h = h;
        } else {
            trap += (max_h - h);
        }
    }
    for (let max_h = 0, i = height.length - 1; i > max_height_pos; i--) {
        let h = height[i];
        if (h > max_h) {
            max_h = h;
        } else {
            trap += (max_h - h);
        }
    }
    return trap;
};