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

  return (
    <main className="min-h-screen bg-[#fafafa] text-zinc-900 [background-image:radial-gradient(#d4d4d8_1px,transparent_1px)] [background-size:18px_18px]">
      <section className="mx-auto max-w-3xl px-5 py-16 sm:py-24">
        <div className="mb-10 flex h-2 w-full overflow-hidden rounded-full">
          <div className="w-2/3 bg-red-500" />
          <div className="w-1/3 bg-yellow-400" />
        </div>

        <Link
          href="/"
          className="mb-12 inline-block text-sm text-zinc-500 transition hover:text-zinc-900"
        >
          ← Back
        </Link>

        <article className="bg-white/75 px-6 py-10 shadow-sm backdrop-blur-sm sm:px-8">
          <div className="mb-6 flex flex-wrap items-center gap-3 text-xs text-zinc-500">
            <time>{post.created_at}</time>

            {post.tags?.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {post.tags.map((tag) => (
                  <span key={tag}>#{tag}</span>
                ))}
              </div>
            )}
          </div>

          <h1 className="mb-10 text-4xl font-bold leading-tight tracking-tight sm:text-5xl">
            {post.title}
          </h1>

          <div className="whitespace-pre-line text-[17px] leading-9 text-zinc-700">
            {post.comment}
          </div>

          <div className="mt-12 flex flex-wrap gap-3 text-xs text-zinc-400">
            <span>keyword: {post.keyword}</span>
            <span>score: {post.trend_score}</span>
          </div>
        </article>
      </section>
    </main>
  );
}