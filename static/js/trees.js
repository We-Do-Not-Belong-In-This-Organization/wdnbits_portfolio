const FROM_PAGE = "{{ from_page }}";
        
function binaryTree() {
    window.location.href = "/binary-tree?from_page=" + encodeURIComponent(FROM_PAGE);
}

function binarySearchTree() {
    window.location.href = "/binary-search-tree?from_page=" + encodeURIComponent(FROM_PAGE);
}

function graph() {
    window.location.href = "/graph?from_page=" + encodeURIComponent(FROM_PAGE);
}