export default async function ProductPage({
  params,
}: {
  params: Promise<{ productId: string }>;
}) {
  const { productId } = await params;
  return <p>Product: {productId}</p>;
}
