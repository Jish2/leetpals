export const getHost = (url: string): [string | null, Error | null] => {
	try {
		const host = new URL(url).host;

		console.log(url, new URL(url));
		return [host, null];
	} catch (err) {
		return [null, err as Error];
	}
};
