import { getUsers } from "@/utils/github";
import { getBadge } from "@/utils/leetcode";
import { getHost } from "@/utils/url";
import { type NextRequest } from "next/server";

export async function GET(request: NextRequest) {
	const hostRaw = request.nextUrl.searchParams.get("host");
	if (!hostRaw) return Response.json({ message: "missing host" }, { status: 400 });

	const hostUrl = hostRaw.startsWith("http") ? hostRaw : "https://" + hostRaw;
	const [host, hostErr] = getHost(hostUrl);
	if (hostErr) return Response.json({ message: "invalid host" }, { status: 400 });

	const users = await getUsers();

	const user = users.find((user) => getHost(user.url)[0] === host);
	if (!user) return Response.json({ message: "user doesn't exist" }, { status: 404 });

	const badgeUrl = await getBadge(user.lc_username);

	const imageResponse = await fetch(badgeUrl);

	if (!imageResponse.ok) return new Response("Image fetch failed", { status: 500 });

	const contentType = imageResponse.headers.get("content-type") || "image/jpeg";

	return new Response(imageResponse.body, {
		headers: {
			"Content-Type": contentType,
			"Cache-Control": "public, max-age=3600",
			"Access-Control-Allow-Origin": "*",
		},
	});
}
