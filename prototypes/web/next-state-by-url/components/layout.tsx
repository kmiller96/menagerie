/** Centers the children in the middle of the container. */
export function Center({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex flex-col flex-grow items-center justify-center">
      {children}
    </div>
  );
}
