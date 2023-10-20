var minimumRecolors = function(blocks, k) {
    let cur = 0;
    
    // Count the initial "W" blocks up to position k
    for (let i = 0; i < k; i++) {
        if (blocks[i] === "W") {
            cur++;
        }
    }

    let minimum = cur;

    // Iterate through the remaining blocks
    for (let i = k; i < blocks.length; i++) {
        // If there's a color change, adjust cur
        if (blocks[i] !== blocks[i - k]) {
            if (blocks[i] === "W") {
                cur++;
            } else {
                cur--;
            }
        }

        minimum = Math.min(minimum, cur);
    }

    return minimum;
};
