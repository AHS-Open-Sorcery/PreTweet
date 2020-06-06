import dayjs from 'dayjs';

export function formatDateTime(date: Date): string {
    return dayjs(date).format('YYYY-MM-DD hh:mm A');
}

export function quantifyAmount(amount: number): string {
    const categories: [number, string][] = [
        [0.9, 'extremely'],
        [0.75, 'very'],
        [0.5, 'moderately'],
        [0.3, 'somewhat'],
        [0.1, 'a little'],
        [0.0, 'not']
    ];
    for (const [threshold, quantifier] of categories) {
        if (amount > threshold) {
            return quantifier;
        }
    }
    return '';
}

export function colorRating(rating: number): string {
    const hue = Math.round(rating * 120);
    return `hsl(${hue}, 100%, 26%)`;
}

export function iconRating(rating: number): string {
    if (rating > 0.6) return 'add';
    else if (rating < 0.4) return 'remove';
    return '';
}