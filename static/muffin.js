// Delete Cupcake
$('.delete-cupcake').click(deleteCupcake);

async function deleteCupcake() {
    const id = $(this).data('id');
    await axios.delete(`/api/cupcakes/${id}`);
    $(this).closest('tr').remove();
}


// Update Cupcake
$('.update-cupcake').click(updateCupcake);

async function updateCupcake() {
    const id = $(this).data('id');

    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    await axios.patch(`/api/cupcakes/${id}`, {
        flavor,
        rating,
        size,
        image
    });
    window.location.replace("/");
}

// Add Cupcake
$("#new-cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();

    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    await axios.post(`/api/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });
    window.location.replace("/");
});
