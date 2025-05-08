function divide(dividend: number, divisor: number): number {
    if (dividend === -2147483648 && divisor === -1) {
        return 2147483647;
    }
    if (divisor === 1) {
        return dividend;
    }
    if (divisor === -1) {
        return -dividend;
    }

    let quotient = ``;
    const stringDividend = `${Math.abs(dividend)}`;
    let remainder = 0;
    const isNegativeQuotient = (dividend < 0 && divisor > 0) ||
        (dividend > 0 && divisor < 0)

    for (let index = 0; index < stringDividend.length; index++) {
        remainder = parseInt(`${remainder}` + stringDividend[index], 10);

        let currentQuotient = 0; 
        while (remainder >= Math.abs(divisor)) {
            currentQuotient += 1;
            remainder = remainder - Math.abs(divisor);
        }

        quotient = quotient + `${currentQuotient}`

        if (
            !isNegativeQuotient &&
            parseInt(quotient, 10) >= (2**31 - 1)
        ) {
            quotient = `${2**31 - 1}`
            break;
        }
        if (
            isNegativeQuotient &&
            parseInt(quotient, 10) >= 2**31
        ) {
            quotient = `${2**31}`
            break;
        }
    }

    return parseInt(
        isNegativeQuotient
            ? `-` + quotient
            : quotient,
        10,
    );
};
