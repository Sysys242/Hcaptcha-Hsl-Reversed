<p align="center">
  <b>🖤 HSL Fingerprint Script by hcaptcha reversed, notice that it will give a lot of fail due to me removed a lot of things, it's pretty simple ( took me less than 1hours ), so enjoy :) 🖤</b><br>
  <br><br>
  <img src="https://cdn.discordapp.com/attachments/762750100500906044/860549000939831316/183296.gif">
    <br><br>
  <b>🖤 Here is js & python version :) 🖤</b><br>
  <b>Original Script: https://newassets.hcaptcha.com/c/6fdd2f3/hsl.js</b><br>
</p>

python (outdated )
```
    def getHsl(proofData) -> str:
        token = proofData['req'].split('.')[1]
        token += '=' * (4 - len(token) % 4)
        tokenJson = json.loads(base64.urlsafe_b64decode(token))
        dt = datetime.utcnow().replace(microsecond=0).isoformat().replace('-', '').replace(':', '').replace('T', '')
        return f"1:{tokenJson['s']}:{dt}:{tokenJson['d']}::2"
```

js/nodejs
```
var hsl = function(token) {
    var sha1 = {
        hash: function (t) {
          if ('string' != typeof t) {
            throw new Error('Message Must Be String')
          }
          for (
            var e = [1518500249, 1859775393, 2400959708, 3395469782],
              n = [1732584193, 4023233417, 2562383102, 271733878, 3285377520],
              o = unescape(encodeURIComponent(t)),
              a = (o += String.fromCharCode(128)).length / 4 + 2,
              i = Math.ceil(a / 16),
              s = new Array(i),
              u = 0;
            u < i;
            u++
          ) {
            s[u] = new Array(16)
            for (var c = 0; c < 16; c++) {
              s[u][c] =
                (o.charCodeAt(64 * u + 4 * c + 0) << 24) |
                (o.charCodeAt(64 * u + 4 * c + 1) << 16) |
                (o.charCodeAt(64 * u + 4 * c + 2) << 8) |
                (o.charCodeAt(64 * u + 4 * c + 3) << 0)
            }
          }
          s[i - 1][14] = (8 * (o.length - 1)) / Math.pow(2, 32)
          s[i - 1][14] = Math.floor(s[i - 1][14])
          s[i - 1][15] = (8 * (o.length - 1)) & 4294967295
          for (var f = 0; f < i; f++) {
            for (var h = new Array(80), l = 0; l < 16; l++) {
              h[l] = s[f][l]
            }
            for (var g = 16; g < 80; g++) {
              h[g] = sha1.rotateLeft(h[g - 3] ^ h[g - 8] ^ h[g - 14] ^ h[g - 16], 1)
            }
            for (
              var d = n[0], v = n[1], p = n[2], w = n[3], y = n[4], S = 0;
              S < 80;
              S++
            ) {
              var C = Math.floor(S / 20),
                T = (sha1.rotateLeft(d, 5) + sha1.f(C, v, p, w) + y + e[C] + h[S]) >>> 0
              y = w
              w = p
              p = sha1.rotateLeft(v, 30) >>> 0
              v = d
              d = T
            }
            n[0] = (n[0] + d) >>> 0
            n[1] = (n[1] + v) >>> 0
            n[2] = (n[2] + p) >>> 0
            n[3] = (n[3] + w) >>> 0
            n[4] = (n[4] + y) >>> 0
          }
          return n
        },
        digest: function (r) {
          return [
            (r[0] >> 24) & 255,
            (r[0] >> 16) & 255,
            (r[0] >> 8) & 255,
            255 & r[0],
            (r[1] >> 24) & 255,
            (r[1] >> 16) & 255,
            (r[1] >> 8) & 255,
            255 & r[1],
            (r[2] >> 24) & 255,
            (r[2] >> 16) & 255,
            (r[2] >> 8) & 255,
            255 & r[2],
            (r[3] >> 24) & 255,
            (r[3] >> 16) & 255,
            (r[3] >> 8) & 255,
            255 & r[3],
            (r[4] >> 24) & 255,
            (r[4] >> 16) & 255,
            (r[4] >> 8) & 255,
            255 & r[4],
          ]
        },
        hex: function (r) {
          for (var t = [], e = 0; e < r.length; e++) {
            t.push(('00000000' + r[e].toString(16)).slice(-8))
          }
          return t.join('')
        },
        rotateLeft: function (r, t) {
          return (r << t) | (r >>> (32 - t))
        },
        f: function (r, t, e, n) {
          switch (r) {
            case 0:
              return (t & e) ^ (~t & n)
            case 1:
            case 3:
              return t ^ e ^ n
            case 2:
              return (t & e) ^ (t & n) ^ (e & n)
          }
        },
      }

      function checkBitPattern(input, hashInput) {
        var bitArray = [];
        for (var i = 0; i < 8 * hashInput.length; i++) {
          var bit = (hashInput[Math.floor(i / 8)] >> i % 8) & 1;
          bitArray.push(bit);
        }
        var relevantBits = bitArray.slice(0, input);
        return 0 == relevantBits[0] && (relevantBits.indexOf(1) >= input - 1 || -1 == relevantBits.indexOf(1));
      }

      function n(t, e) {
        var n,o;
        return checkBitPattern(t, ((n = e), (o = sha1.hash(n)), sha1.digest(o)))
    }  
    
    function incrementLastValue(arr) {
        for (var i = arr.length - 1; i >= 0; i--) {
          if (arr[i] < 61) {
            return ++arr[i], true;
          }
          arr[i] = 0;
        }
        return false;
    }

    function buildStringFromIndex(r) {
        var str = '0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        return r.reduce((e, i) => e + str[i], '');
    }

    function findValue(r, t) {
        for (var e = 0; e < 25; e++) {
          var i = new Array(e).fill(0);
          while (incrementLastValue(i)) {
            if (n(r, t + '::' + buildStringFromIndex(i))) {
              return buildStringFromIndex(i);
            }
          }
        }
    }
    var tokenSplitted = JSON.parse(atob(token.split('.')[1]));
    return `1:${tokenSplitted.s}:${new Date().toISOString().slice(0, 19).replace(/[-:T]/g, '')}:${tokenSplitted.d}::${findValue(tokenSplitted.s, tokenSplitted.d)}`
} 
```
