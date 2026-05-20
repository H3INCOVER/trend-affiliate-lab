import posts from "@/data/published_posts.json";
import Link from "next/link";
import { notFound } from "next/navigation";

type Post = {
  title: string;
  slug: string;
  tags: string[];
  comment: string;
  keyword: string;
  trend_score: number;
  created_at: string;
};

type Props = {
  params: Promise<{
    slug: string;
  }>;
};

export default async function PostPage({ params }: Props) {
  const { slug } = await params;

  const allPosts = posts as Post[];
  const post = allPosts.find((p) => p.slug === slug);

  if (!post) {
    notFound();
  }

  const relatedPosts = allPosts
    .filter((p) => p.slug !== post.slug)
    .filter((p) =>
      p.tags?.some((tag) => post.tags?.includes(tag))
    )
    .slice(0, 3);

  return (
    <div className="min-h-screen bg-[#fafafa] text-zinc-900 [background-image:radial-gradient(#d4d4d8_1px,transparent_1px)] [background-size:18px_18px]">
      <section className="mx-auto max-w-4xl px-5 py-14 sm:py-20">
        <div className="mb-10 flex h-2 w-full overflow-hidden rounded-full">
          <div className="w-2/3 bg-red-500" />
          <div className="w-1/3 bg-yellow-400" />
        </div>

        <Link
          href="/"
          className="mb-10 inline-flex items-center text-sm font-medium text-zinc-500 transition hover:text-zinc-900"
        >
          ← 記事一覧へ戻る
        </Link>

        <article className="rounded-[2rem] border border-zinc-200 bg-white/85 px-6 py-10 shadow-sm backdrop-blur-sm sm:px-10 sm:py-14">
          <div className="mb-7 flex flex-wrap items-center gap-3 text-xs font-medium text-zinc-500">
            <time>{post.created_at}</time>

            {post.tags?.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {post.tags.map((tag) => (
                  <span
                    key={tag}
                    className="rounded-full bg-zinc-100 px-3 py-1 text-zinc-600"
                  >
                    #{tag}
                  </span>
                ))}
              </div>
            )}
          </div>

          <h1 className="mb-10 text-3xl font-black leading-tight tracking-tight text-zinc-950 sm:text-5xl">
            {post.title}
          </h1>

          <div className="border-y border-zinc-200 py-8">
            <div className="whitespace-pre-line text-[17px] leading-9 text-zinc-700 sm:text-lg sm:leading-10">
              {post.comment}
            </div>
          </div>

          <div className="mt-10 grid gap-3 rounded-2xl bg-zinc-50 p-5 text-sm text-zinc-600 sm:grid-cols-2">
            <div>
              <p className="mb-1 text-xs font-bold uppercase tracking-widest text-zinc-400">
                Keyword
              </p>
              <p className="font-medium text-zinc-800">{post.keyword}</p>
            </div>

            <div>
              <p className="mb-1 text-xs font-bold uppercase tracking-widest text-zinc-400">
                Trend Score
              </p>
              <p className="font-medium text-zinc-800">{post.trend_score}</p>
            </div>
          </div>
        </article>

        {relatedPosts.length > 0 && (
          <section className="mt-14">
            <div className="mb-6 flex items-end justify-between gap-4">
              <div>
                <p className="mb-2 text-xs font-bold tracking-[0.25em] text-red-500">
                  RELATED
                </p>
                <h2 className="text-2xl font-black text-zinc-900">
                  関連記事
                </h2>
              </div>

              <Link
                href="/"
                className="text-sm font-medium text-zinc-500 transition hover:text-zinc-900"
              >
                一覧を見る
              </Link>
            </div>

            <div className="grid gap-4">
              {relatedPosts.map((related) => (
                <Link
                  key={related.slug}
                  href={`/posts/${related.slug}`}
                  className="group rounded-3xl border border-zinc-200 bg-white/80 p-6 shadow-sm transition hover:-translate-y-0.5 hover:bg-white hover:shadow-md"
                >
                  <div className="mb-3 flex flex-wrap items-center gap-2 text-xs text-zinc-500">
                    <time>{related.created_at}</time>

                    {related.tags?.slice(0, 3).map((tag) => (
                      <span key={tag}>#{tag}</span>
                    ))}
                  </div>

                  <h3 className="text-lg font-bold leading-snug text-zinc-900 group-hover:text-red-500">
                    {related.title}
                  </h3>
                </Link>
              ))}
            </div>
          </section>
        )}
      </section>
    </div>
  );
}