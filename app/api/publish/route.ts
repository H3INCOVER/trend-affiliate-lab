import { NextResponse } from "next/server";

import fs from "fs";
import path from "path";

type Post = {
  title: string;
  tags: string[];
  comment: string;
  keyword: string;
  trend_score: number;
  created_at: string;
};

export async function POST(req: Request) {
  try {
    const post = (await req.json()) as Post;

    const publishedPath = path.join(
      process.cwd(),
      "data",
      "published_posts.json"
    );

    const current = JSON.parse(
      fs.readFileSync(publishedPath, "utf-8")
    ) as Post[];

    const alreadyPublished = current.some((item) => {
      return (
        item.keyword === post.keyword &&
        item.created_at === post.created_at
      );
    });

    if (alreadyPublished) {
      return NextResponse.json({
        success: false,
        message: "すでに公開済みです",
      });
    }

    current.unshift(post);

    fs.writeFileSync(
      publishedPath,
      JSON.stringify(current, null, 2),
      "utf-8"
    );

    return NextResponse.json({
      success: true,
      message: "公開へ追加しました",
    });
  } catch (error) {
    console.error(error);

    return NextResponse.json(
      {
        success: false,
        message: "公開に失敗しました",
      },
      {
        status: 500,
      }
    );
  }
}