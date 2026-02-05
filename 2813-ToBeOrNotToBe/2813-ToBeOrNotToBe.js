// Last Updated: 2/5/2026, 9:21:37 AM
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(newValue){
            if (val===newValue) return true;
            else throw new Error('Not Equal');
        },
        notToBe: function(newValue){
            if (val!==newValue) return true;
            else throw new Error('Equal');
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */