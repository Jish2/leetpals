import { load } from "js-yaml";

export interface User {
	username: string;
	url: string;
	lc_username: string;
}

const url = "https://raw.githubusercontent.com/Jish2/leetpals/refs/heads/main/sites.yaml";

export const getUsers = async () => {
	const data = await fetch(url);
	const text = await data.text();
	const users = load(text) as User[];

	return users;
};
