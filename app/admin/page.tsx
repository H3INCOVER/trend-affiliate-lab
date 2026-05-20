"use client";

import { useState } from "react";

import draftPosts from "../../data/draft_posts.json";

type Post = {
  title: string;
  tags: string[];
  comment: string;
  keyword: string;
  trend_score: number;
  created_at: string;
};

const posts = draftPosts as Post[];

export default function AdminPage() {
  const [editedComments, setEditedComments] = useState<Record<string, string>>(
    {}
  );

  const getPostKey = (post: Post) => {
    return `${post.keyword}-${post.created_at}`;
  };

  const publishPost = async (post: Post) => {
    const key = getPostKey(post);
    const editedComment = editedComments[key]?.trim();

    const postToPublish = {
      ...post,
      comment: editedComment || post.comment,
    };

    const res = await fetch("/api/publish", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(postToPublish),
    });

    const data = await res.json();

    alert(data.message || (data.success ? "公開へ追加しました" : "公開失敗"));
  };

  return (
    <main className="min-h-screen bg-zinc-50 text-black">
      <section className="border-b border-zinc-200 bg-white">
        <div className="mx-auto max-w-7xl px-6 py-16">
          <p className="mb-3 text-xs font-bold uppercase tracking-[0.2em] text-red-500">
            Admin
          </p>

          <h1 className="text-5xl font-black tracking-tight">
            Draft Observation Posts
          </h1>

          <p className="mt-4 text-zinc-600">自動生成された観測候補一覧</p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-7xl px-6 py-10">
          <div className="space-y-6">
            {posts.map((post) => {
              const key = getPostKey(post);

              return (
                <article
                  key={key}
                  className="rounded-3xl border border-zinc-200 bg-white p-8"
                >
                  <div className="mb-5 flex flex-wrap items-center justify-between gap-3">
                    <div className="flex flex-wrap gap-2">
                      {post.tags.map((tag) => (
                        <span
                          key={tag}
                          className="rounded-full bg-zinc-100 px-3 py-1 text-xs font-bold text-zinc-700"
                        >
                          #{tag}
                        </span>
                      ))}
                    </div>

                    <span className="text-xs font-bold text-zinc-400">
                      score: {post.trend_score}
                    </span>
                  </div>

                  <h2 className="mb-4 text-3xl font-black leading-tight tracking-tight">
                    {post.title}
                  </h2>

                  <p className="mb-6 text-sm text-zinc-400">
                    keyword: {post.keyword}
                  </p>

                  <p className="whitespace-pre-line leading-8 text-zinc-700">
                    {post.comment}
                  </p>

                  <div className="mt-6">
                    <p className="mb-2 text-xs font-bold uppercase tracking-[0.2em] text-zinc-400">
                      公開用編集欄
                    </p>

                    <textarea
                      value={editedComments[key] || ""}
                      onChange={(e) =>
                        setEditedComments((prev) => ({
                          ...prev,
                          [key]: e.target.value,
                        }))
                      }
                      placeholder="ChatGPT / Geminiで書き直した文章を貼る。空欄なら元の文章で公開。"
                      className="min-h-[220px] w-full rounded-2xl border border-zinc-300 p-4 text-sm leading-7 text-zinc-700 outline-none transition focus:border-black"
                    />
                  </div>

                  <div className="mt-8 flex flex-wrap gap-3">
                    <button
                      onClick={() => publishPost(post)}
                      className="rounded-2xl bg-black px-5 py-3 text-sm font-bold text-white transition hover:bg-red-500"
                    >
                      公開する
                    </button>

                    <button className="rounded-2xl border border-zinc-300 bg-white px-5 py-3 text-sm font-bold text-black transition hover:border-black">
                      AIで書き直す
                    </button>
                  </div>
                </article>
              );
            })}
          </div>
        </div>
      </section>
    </main>
  );
}