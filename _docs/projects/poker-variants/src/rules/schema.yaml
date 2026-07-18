name: string
type: poker | non-poker
deck:
  decks: 1
  jokers: 0
dealing:
  cardsPerPlayer: number
  streets:
    - name: string
      face: down | up | mixed
      count: number
      options:
        buyUpcard:
          cost: number
          condition: string
        blind: boolean
draw:
  rounds:
    - maxDiscard: number
      targetHandSize: number
      betweenBets: boolean
passing:
  rounds:
    - count: number
      direction: left | right
      source: player | deckIfLast
betting:
  opener:
    type: none | rankAtLeast
    rank: optional
  winCondition:
    type: standard | rankAtLeast
    rank: optional
  rounds:
    - name: string
      forceBet?: number
sidePots:
  - name: string
    ante: number
    trigger: onBet | onAnte | fixed
    contribution: fixed | mirrorMain
    resolver: string
wilds:
  - type: static | ascending | lowHole | spit | rankSet
    value: details vary by type
sharedBoard:
  layout:
    type: cross | line | none
    cards: 5
    revealSchedule:
      - when: string
        face: up | down
        role: centerWild | cornerOnly
handEval:
  acesHigh: boolean
  straightsWrap: boolean
  rankings: standard | custom
tieRules:
  split: true
  special: []
misc:
  notes: string
