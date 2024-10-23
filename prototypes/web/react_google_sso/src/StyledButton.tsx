export function StyledButton(
  props: React.ButtonHTMLAttributes<HTMLButtonElement>
) {
  return (
    <button
      style={{
        fontSize: 18,
        marginTop: 5,
        marginBottom: 5,
        paddingLeft: 15,
        paddingRight: 15,
        borderRadius: "8px",
        backgroundColor: "white",
        boxShadow: "3px 3px rgba(0,0,0,0.2)",
        ...props,
      }}
      {...props}
    />
  );
}
