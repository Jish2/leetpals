export const getHost = (url: string): [string | null, Error | null] => {
	try {
		const host = new URL(url).host;
		return [host, null];
	} catch (err) {
		return [null, err as Error];
	}
};
