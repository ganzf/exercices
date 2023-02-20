import { waaagh } from './step1';

describe('step1', () => {
    it('should have a function named "waaagh"', () => {
        expect(waaagh).toBeDefined();
        // check waaagh prototype
        expect(typeof waaagh).toBe('function');
        // check return type
        const list = waaagh(0);
        expect(list).toBe([]);
    });

    it('should return a grumblzock', () => {
        const list = waaagh(16);
        expect(list).toEqual([
            'waagh1',
            'waagh2',
            'grumbl',
            'waagh4',
            'zock',
            'grumbl',
            'waagh7',
            'waagh8',
            'grumbl',
            'zock',
            'waagh11',
            'grumbl',
            'waagh13',
            'waagh14',
            'grumblzock',
            'waagh16',
        ]);
    });

    it('test with large number', () => {
        const list = waaagh(1000);
        expect(list.length).toBe(1000);
        expect(list[14]).toBe('grumblzock')
        expect(list[29]).toBe('grumblzock')
        expect(list[44]).toBe('grumblzock')
        expect(list[59]).toBe('grumblzock')
        expect(list[2]).not.toBe('grumblzock');
    })
});