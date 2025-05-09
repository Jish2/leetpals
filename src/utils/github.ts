import { load } from "js-yaml";

export interface User {
	username: string;
	url: string;
	lc_username: string;
}

const url = "https://raw.githubusercontent.com/Jish2/leetpals/refs/heads/main/sites.yaml";

export const getUsers = async () => {
	const data = await fetch(url, { cache: "no-store" });
	const text = await data.text();
	const users = load(text) as User[];
	console.log("users", users)
	return users;
};
