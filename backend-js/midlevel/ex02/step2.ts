export type OrcType = 'Melee' | 'Ranged' | 'Dummy';

export interface Orc {
    number: number;
    type: OrcType;
}

export class Battalion {
    number: number;
    row1: Orc[] = [];
    row2: Orc[] = [];
    row3: Orc[] = [];

    constructor(number: number) {
        this.number = number;
    }

    getRow1(): OrcType[] {
        return this.row1.map(o => o.type);
    }

    getRow2(): OrcType[] {
        return this.row2.map(o => o.type);
    }

    getRow3(): OrcType[] {
        return this.row3.map(o => o.type);
    }
}

export function organizeBattle(Orcs: Orc[]): Battalion[] {
    const battalions: Battalion[] = [];
    const ranged = Orcs.filter(o => o.type === 'Ranged');
    const melee = Orcs.filter(o => o.type === 'Melee');
    const dummy = Orcs.filter(o => o.type === 'Dummy');
    const b = new Battalion(1);
    battalions.push(b);
    for (let i = 0; i < 3; i++) {
        b.row1.push(melee[i]);
        b.row2.push(dummy[i]);
        b.row3.push(ranged[i]);
    }
    return battalions;
}