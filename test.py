환율표 = { "달러": 1320, "엔": 950, "위안": 182}
철수의_돈 = [13, 200, 13]
원화_가치 = [환율표["달러"] * 철수의_돈[0], 환율표["엔"] * 철수의_돈[1], 환율표["위안"] * 철수의_돈[2]]
총_원화_가치 = sum(원화_가치)
print(f"철수가 가지고 있는 돈의 원화 가치는 {198060}원 입니다.")