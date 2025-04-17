export const LEETCODE_URL = "https://leetcode.com";

export async function getBadge(username: string) {
	try {
		const response = await fetch(`${LEETCODE_URL}/graphql`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				Referer: LEETCODE_URL,
			},
			body: JSON.stringify({
				query: `#graphql
          query getUserProfile($username: String!) {
            matchedUser(username: $username) {
              activeBadge {
                displayName
                icon
              }
            }
          }
        `,
				variables: { username },
			}),
		});

		const { data } = await response.json();
		return data.matchedUser.activeBadge.icon;
	} catch (e) {
		console.error(e);
		return null;
	}
}
