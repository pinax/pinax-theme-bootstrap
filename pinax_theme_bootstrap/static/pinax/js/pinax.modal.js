(function($) {
    var Modal = function(oe, options) {
        this.oe = oe;
        this.settings = $.extend({}, $.fn.modal.defaults);
        if (options) {
            $.extend(this.settings, options);
        }
        return this;
    }
    Modal.prototype = {
        toggle: function () {
            return this[!this.is_open ? "open" : "close"]();
        },
        populate: function(url) {
            var that = this;
            this.$modal.load(url, function() {
                that.ajaxify(that.$modal);
            });
        },
        open: function () {
            var that = this;
            this.is_open = true;
            this.$modal = $("#modal-popup");
            this.populate(this.oe.attr("href"));
            if (this.settings.backdrop) {
                this.$backdrop = $('<div id="modal-backdrop" class="modal-backdrop" />');
                this.$backdrop.click(function () {
                    that.close();
                });
                this.$backdrop.appendTo("#modal");
            }
            // .close class in modal can close itself
            this.$modal.delegate(".modal-close", "click", function (e) {
                e.preventDefault();
                that.close();
            });
            // bind esc to close
            $(window).bind("keyup.modal.escape", function (e) {
                if (e.which == 27) {
                    that.close();
                }
            });
            $("#modal").fadeIn(200);
        },
        close: function () {
            var that = this;
            this.is_open = false;
            if (this.close_redirect) {
                window.location.href = this.close_redirect;
            } else {
                $("#modal").fadeOut(200, function() {
                    $("#modal").remove();
                    that.$modal = null;
                    if (that.settings.backdrop) {
                        that.$backdrop = null;
                    }
                    $(window).unbind("keyup.modal.escape");
                });
            }
        },
        ajaxify: function (modal) {
            var that = this;
            modal.find("a.ajax").click(function(e) {
                e.preventDefault();
                that.populate($(this).attr("href"));
            }).removeClass("ajax");
            if ($.fn.ajaxForm) {
                $("form.ajax", modal).ajaxForm({
                    dataType: "json",
                    success: function (data) {
                        if (data.html) {
                            if (data.location) {
                                that.close_redirect = data.location;
                            }
                            modal.html(data.html);
                            that.ajaxify(that.$modal);
                        } else {
                            if (data.location) {
                                window.location.href = data.location;
                            }
                        }
                    }
                });
            }
        }
    }
    $.fn.modal = function(options) {
        options = options || {}
        var modal = new Modal(this, options);
        $(this).click(function(e) {
            e.preventDefault();
            $("body").append('<div id="modal" style="display: none;"></div>');
            $("#modal").append('<div id="modal-popup" class="modal"></div>');
            modal.open();
        });
        return modal;
    }
    $.fn.modal.defaults = {
        backdrop: false
    }
})(jQuery)
