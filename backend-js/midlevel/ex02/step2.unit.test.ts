import { organizeBattle } from "./step2";

function createOrcs(type: any, amount: number): any[] {
    const orcs: any[] = [];
    for (let i = 0; i < amount; i++) {
        const orc = { number: i + 1, type };
        orcs.push(orc);
    }
    return orcs;
}

describe('Step 2: Orc battalions', () => {
    it('should be able to fill battalions', () => {
        const orcs: any[] = [];
        const orc1 = { number: 1, type: 'Melee' };
        const orc2 = { number: 2, type: 'Ranged' };
        const orc3 = { number: 3, type: 'Dummy' };
        const orc4 = { number: 4, type: 'Melee' };
        const orc5 = { number: 5, type: 'Ranged' };
        const orc6 = { number: 6, type: 'Dummy' };
        const orc7 = { number: 7, type: 'Melee' };
        const orc8 = { number: 8, type: 'Ranged' };
        const orc9 = { number: 9, type: 'Dummy' };
        orcs.push(orc1, orc2, orc3, orc4, orc5, orc6, orc7, orc8, orc9);
        const battalions = organizeBattle(orcs);
        expect(battalions.length).toBe(1);
        const one = battalions[0].getRow1();
        expect(one).toEqual(['Melee', 'Melee', 'Melee']);
        const two = battalions[0].getRow2();
        expect(two).toEqual(['Dummy', 'Dummy', 'Dummy']);
        const three = battalions[0].getRow3();
        expect(three).toEqual(['Ranged', 'Ranged', 'Ranged']);
    });

    it('should fill 2 battalions and leave orcs behind', () => {
        const orcs = [
            ...createOrcs('Melee', 6),
            ...createOrcs('Ranged', 7),
            ...createOrcs('Dummy', 6),
        ]
        const battalions = organizeBattle(orcs);
        expect(battalions.length).toBe(2);
    })

    it('should not fill any with no ranged', () => {
        const orcs = [
            ...createOrcs('Melee', 6),
            ...createOrcs('Dummy', 6),
        ]
        const battalions = organizeBattle(orcs);
        expect(battalions.length).toBe(0);
    });

    it('should be able to make a battalion with 6 melee and 1 ranged', () => {
        const orcs = [
            ...createOrcs('Melee', 6),
            ...createOrcs('Ranged', 3),
        ]
        const battalions = organizeBattle(orcs);
        expect(battalions.length).toBe(1);
    });
})