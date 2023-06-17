import winsound as ws
ws.Beep(440,1000)
# ws.Beep(494,1000)
# # 声音长度小于1秒，竟然播放不出声音？？？
# ws.Beep(880,1000)
ws.PlaySound('music.wav',ws.SND_FILENAME)

# ws.PlaySound('music.wav', ws.SND_FILENAME | ws.SND_ASYNC | ws.SND_ALIAS)

# Play Windows exit sound.
# ws.PlaySound("SystemExit", ws.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
# ws.PlaySound("*", ws.SND_ALIAS)
