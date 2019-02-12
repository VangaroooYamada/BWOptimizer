# TODO

## Optimizer

- 渡されたグラフ情報から最適ルートを返す
  - 最短ルート(nodeコストを加味せず通るnode数を最小に)
  - 最適ルート(通るnodeの合計コストを最小に)
  - 選別ルート(指定されたnode typeを優先して回る[追い追い？])
- グラフの情報
  - 各nodeのコスト(3-7,None)
  - 各nodeの種類(perk, item, addon, offering)
  - 各node間のedgeの有無
- Entityの挙動
