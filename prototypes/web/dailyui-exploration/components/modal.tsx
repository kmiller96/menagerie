"use client";

const MODAL_ID = "my_modal_1";

export function Modal() {
  return (
    <>
      <ModalButton />
      <ModalContent />
    </>
  );
}

function ModalButton() {
  return (
    <button
      className="btn"
      onClick={() => {
        const modal = document.getElementById(MODAL_ID) as HTMLDialogElement;
        modal.showModal();
      }}
    >
      open modal
    </button>
  );
}

function ModalContent() {
  return (
    <dialog id="my_modal_1" className="modal">
      <div className="modal-box">
        <h3 className="font-bold text-lg">Hello!</h3>
        <p className="py-4">Press ESC key or click the button below to close</p>
        <div className="modal-action">
          <form method="dialog">
            {/* if there is a button in form, it will close the modal */}
            <button className="btn">Close</button>
          </form>
        </div>
      </div>
    </dialog>
  );
}
