import { getUsers } from "@/utils/github";
import { getHost } from "@/utils/url";
import { type NextRequest } from "next/server";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
	const hostRaw = request.nextUrl.searchParams.get("host");
	if (!hostRaw) return Response.json({ message: "missing host" }, { status: 400 });

	const hostUrl = hostRaw.startsWith("http") ? hostRaw : "https://" + hostRaw;
	const [host, hostErr] = getHost(hostUrl);
	if (hostErr) return Response.json({ message: "invalid host" }, { status: 400 });

	const users = await getUsers();

	const exists = users.findIndex((user) => getHost(user.url)[0] === host);
	if (exists === -1) return Response.json({ message: "user doesn't exist" }, { status: 404 });

	const nextIndex = (exists + 1) % users.length;
	const nextUser = users[nextIndex];

	return Response.redirect(nextUser.url);
}
