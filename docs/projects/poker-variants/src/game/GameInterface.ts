// src/game/GameInterface.ts
export interface PlayerAction {
  type: 'fold' | 'check' | 'call' | 'bet' | 'raise' | 'pay-side' | 'buy-upcard' | 'pass-cards' | 'trade-left' | 'draw';
  amount?: number;
  payload?: any; // e.g., pass counts, choose wild, declare ace high/low, etc.
}

export interface GameInterface {
  initTable(seats: number, stakes: Stakes): void;
  seatPlayer(playerId: string, buyIn: number): void;
  startHand(): void;
  getState(): PublicState;
  getPrivateState(playerId: string): PrivateState;
  getLegalActions(playerId: string): PlayerAction[];
  applyAction(playerId: string, action: PlayerAction): void;
  isHandOver(): boolean;
  settle(): Settlement;
}

export interface Stakes {
  ante?: number;
  bringIn?: number;
  minBet?: number;
  sideAnte?: number; // for side pots like Red Delilah / Spit
}
