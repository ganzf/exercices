// Welcome Warrior !

export function waaagh(orcs: number): string[] {
    const list: string[] = [];
    for (let i = 1; i <= orcs; i++) {
        const a = i % 3;
        const b = i % 5;
        if (a === 0 && b === 0) {
            list.push('grumblzock');
        } else if (a === 0) {
            list.push('grumbl');
        } else if (b === 0) {
            list.push('zock');
        } else {
            list.push(`waagh${i}`);
        }
    }
    return list;
}