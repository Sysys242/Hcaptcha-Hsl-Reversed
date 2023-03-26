<p align="center">
  <b>🖤 HSL Fingerprint Script by hcaptcha reversed, notice that it will give a lot of fail due to me removed a lot of things, it's pretty simple ( took me less than 1hours ), so enjoy :) 🖤</b><br>
  <br><br>
  <img src="https://cdn.discordapp.com/attachments/762750100500906044/860549000939831316/183296.gif">
    <br><br>
  <b>🖤 Here is js & python version :) 🖤</b><br>
</p>

```
    def getHsl(proofData) -> str:
        token = proofData['req'].split('.')[1]
        token += '=' * (4 - len(token) % 4)
        tokenJson = json.loads(base64.urlsafe_b64decode(token))
        dt = datetime.utcnow().replace(microsecond=0).isoformat().replace('-', '').replace(':', '').replace('T', '')
        return f"1:{tokenJson['s']}:{dt}:{tokenJson['d']}::2"
```

```
var hsl = function (token) {
    var tokenJson = JSON.parse(atob(token.split('.')[1]))
    return `1:${tokenJson.s}:${new Date().toISOString().slice(0, 19).replace(/[-:T]/g, '')}:${tokenJson.d}::2`
};
```
