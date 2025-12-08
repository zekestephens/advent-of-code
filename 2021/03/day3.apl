#!/usr/bin/env -S apl --script
]BOXING 4
in←⊃(⍎¨)⎕FIO[49] 'input'
(2⊥~g)×2⊥g←(.5×1⌷⍴in)<+⌿in
∇ c ← Counts v; u
	u←((v⍳v)=⍳⍴v)/v
    c←u,[1.5]+/u∘.=v
∇
)OFF