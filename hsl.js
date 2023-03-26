var hsl = function (token) {
    var tokenJson = JSON.parse(atob(token.split('.')[1]))
    return `1:${tokenJson.s}:${new Date().toISOString().slice(0, 19).replace(/[-:T]/g, '')}:${tokenJson.d}::2`
};