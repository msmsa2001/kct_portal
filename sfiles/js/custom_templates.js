CKEDITOR.addTemplates('default', {
    imagesPath: '/static/img/',  // Optional: if you use images
    templates: [
      {
        title: 'FAQ Dropdown Block',
        description: 'Insert a collapsible FAQ item',
        html:
          '<details>\n' +
          '  <summary><strong>Sample Question?</strong></summary>\n' +
          '  <p>Your answer goes here.</p>\n' +
          '</details>\n' +
          '<hr style="margin: 5px 0; border: none; border-top: 1px solid #ccc;">'
      },
    //   {
    //     title: 'FAQ With List',
    //     description: 'FAQ answer with a bullet list',
    //     html:
    //       '<details>\n' +
    //       '  <summary><strong>What documents are required?</strong></summary>\n' +
    //       '  <ul>\n' +
    //       '    <li>Document 1</li>\n' +
    //       '    <li>Document 2</li>\n' +
    //       '    <li>Document 3</li>\n' +
    //       '  </ul>\n' +
    //       '</details>\n' +
    //       '<hr style="margin: 5px 0; border: none; border-top: 1px solid #ccc;">'
    //   }
    ]
  });
  