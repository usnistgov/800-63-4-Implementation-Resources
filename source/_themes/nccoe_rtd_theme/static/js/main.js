const enableZoomOnEnlargedSVG = (svgElement) => {
  const svg = d3.select(svgElement);

  // wrap the SVG content in a <g> element for transformations
  svg.html("<g class='wrapper'>" + svg.html() + "</g>");
  const inner = svg.select("g");

  const zoom = d3.zoom()
    .scaleExtent([1, 4])
    .on("zoom", function (event) {
      inner.attr("transform", event.transform);
    });

  svg.call(zoom);
};

const disableZoomOnSVG = (svgElement) => {
  const svg = d3.select(svgElement);
  svg.on(".zoom", null);
};

(function () {
  if (!window.SphinxRtdTheme || !window.SphinxRtdTheme.Navigation || !window.jQuery) {
    return;
  }

  const $ = window.jQuery;
  const navigation = window.SphinxRtdTheme.Navigation;
  const resetNavigation = navigation.reset;

  function setExpanded($item, isExpanded) {
    $item
      .toggleClass('expanded', isExpanded)
      .toggleClass('collapsed', !isExpanded)
      .attr('aria-expanded', isExpanded ? 'true' : 'false');

    $item.find('> a').attr('aria-expanded', isExpanded ? 'true' : 'false');
  }

  function collapseItems($items) {
    $items.each(function () {
      setExpanded($(this), false);
    });
  }

  navigation.toggleExpand = function ($link) {
    const $item = $link.closest('li');
    const hasChildItems = $item.find('> ul li').length > 0;

    if (!hasChildItems) {
      return;
    }

    const isExpanded = $item.hasClass('expanded') || $item.attr('aria-expanded') === 'true';

    collapseItems($item.siblings('li.expanded, li.collapsed'));
    collapseItems($item.siblings().find('li.expanded, li.collapsed'));
    collapseItems($item.find('> ul li.expanded, > ul li.collapsed'));
    setExpanded($item, !isExpanded);
  };

  navigation.reset = function () {
    const result = resetNavigation.apply(this, arguments);
    const $currentItems = $('.wy-menu-vertical li.current');

    $currentItems.add($currentItems.parents('li')).each(function () {
      const $item = $(this);
      $item.removeClass('collapsed');
      $item.find('> a').attr('aria-expanded', $item.attr('aria-expanded'));
    });

    return result;
  };
})();

$(document).ready(function () {
  var table = $('table.datatable').DataTable({
    paging: false,
    ordering: true,
    order: [[0, 'asc']],
    searching: true,
    responsive: true,
    autoWidth: false,
  });


  // Reset the select element to its default value on page load
  $('#label-list').val('');

  $('#label-list').on('change', function () {
    var selectedValue = $(this).val();
    if (selectedValue) {
      table.column(2).search(selectedValue).draw();
    } else {
      table.column(2).search('').draw();
    }
  });

  const $overlay = $('<div class="overlay" aria-hidden="true"></div>').appendTo('body');
  const $closeButton = $('<button class="close-button" aria-label="Close enlarged SVG">Close</button>').appendTo('body');

  $('.mermaid').on('click', function (e) {
    const $svg = $(this).find('svg');

    if (!$svg.hasClass('enlarged')) {
      $svg.addClass('enlarged');
      $svg.attr('aria-expanded', 'true');

      disablePageScrolling();

      enableZoomOnEnlargedSVG($svg[0]); //enable zoom after svg is enlarged

      // position the close button relative to the enlarged SVG in the upper right
      const svgRect = $svg[0].getBoundingClientRect();
      $closeButton.css({
        top: svgRect.top,
        left: svgRect.right - 79 + 'px',
      });

      // show the overlay and close button
      $overlay.addClass('active').attr('aria-hidden', 'false');
      $closeButton.addClass('active').attr('aria-hidden', 'false');

      // close button functionality
      $closeButton.on('click', function () {
        closeEnlargedSVG($svg, $closeButton);
      });

      // close when clicking outside the SVG
      $overlay.on('click', function () {
        closeEnlargedSVG($svg, $closeButton);
      });

      // render the close button
      $closeButton.show();
    }

    e.stopPropagation(); // prevent closing when clicking on the SVG itself
  });


  function closeEnlargedSVG($svg, $closeButton) {
    $svg.removeClass('enlarged');
    $svg.attr('aria-expanded', 'false');
    $overlay.removeClass('active').attr('aria-hidden', 'true');
    $closeButton.removeClass('active').attr('aria-hidden', 'true');
    $closeButton.hide();
    disableZoomOnSVG($svg[0]); // disable zoom after svg has been closed
    enablePageScrolling();
  }

  function disablePageScrolling() {
    $('body').css('overflow', 'hidden');
  }

  function enablePageScrolling() {
    $('body').css('overflow', '');
  }

  var $accordionButtons = $('.accordion-button');
  var $expandCollapseAllButton = $('#expand-collapse-all');
  var isExpandedAll = false;

  $accordionButtons.on('click', function () {
    var $this = $(this);
    var $panel = $('#' + $this.attr('aria-controls'));
    var isExpanded = $this.attr('aria-expanded') === 'true';
    console.log("clicked");

    $this.attr('aria-expanded', isExpanded ? 'false' : 'true');
    if (isExpanded) {
      $panel.slideUp(300, function () {
        $panel.attr('hidden', '');
      });
    } else {
      $panel.removeAttr('hidden');
      $panel.hide().slideDown(300);
    }

  });

  $expandCollapseAllButton.on('click', function () {
    isExpandedAll = !isExpandedAll;
    $accordionButtons.attr('aria-expanded', isExpandedAll ? 'true' : 'false');
    if (isExpandedAll) {
      $('.accordion-panel').removeAttr('hidden').hide().slideDown(300);
    } else {
      $('.accordion-panel').slideUp(300, function () {
        $(this).attr('hidden', '');
      });
    }
    $expandCollapseAllButton.text(isExpandedAll ? 'Collapse All' : 'Expand All');
  });

});
