import { sumOfIntegers } from "./exercice1";

describe('Exercice 1', () => {
    it('should return 0 when n is 0', () => {
        expect(sumOfIntegers(0)).toBe(0);
    });
});